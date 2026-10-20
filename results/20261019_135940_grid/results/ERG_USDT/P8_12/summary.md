# EMA Hourly Continuation — ERG/USDT P8_12

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1875 |
| net_profit_factor | 0.1529 |
| net_win_rate | 0.2517 |
| gross_profit_factor | 0.4409 |
| gross_win_rate | 0.3040 |
| sharpe_ratio | -23.4063 |
| sortino_ratio | -15.1906 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 3.8231 |
| net_avg_loss | -8.4137 |
| avg_hold_time_bars | 2.1195 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
