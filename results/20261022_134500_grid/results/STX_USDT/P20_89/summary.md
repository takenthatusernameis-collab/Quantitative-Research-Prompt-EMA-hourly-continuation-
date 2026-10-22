# EMA Hourly Continuation — STX/USDT P20_89

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.6192 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -4.3450 |
| sortino_ratio | -1.6182 |
| max_drawdown | 0.8662 |
| cagr | -0.5382 |
| net_avg_win | 42.3838 |
| net_avg_loss | -60.2153 |
| avg_hold_time_bars | 11.9616 |
| exposure | 0.3805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
