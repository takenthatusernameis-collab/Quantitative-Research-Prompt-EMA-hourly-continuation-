# EMA Hourly Continuation — ERG/USDT P8_20

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1710 |
| net_profit_factor | 0.2178 |
| net_win_rate | 0.3205 |
| gross_profit_factor | 0.4849 |
| gross_win_rate | 0.3485 |
| sharpe_ratio | -17.7791 |
| sortino_ratio | -10.6071 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 5.0809 |
| net_avg_loss | -11.0020 |
| avg_hold_time_bars | 3.0731 |
| exposure | 0.2389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
