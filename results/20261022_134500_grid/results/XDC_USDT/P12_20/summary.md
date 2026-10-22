# EMA Hourly Continuation — XDC/USDT P12_20

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.1140 |
| net_win_rate | 0.3008 |
| gross_profit_factor | 0.4745 |
| gross_win_rate | 0.3943 |
| sharpe_ratio | -19.3064 |
| sortino_ratio | -11.1088 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 2.9190 |
| net_avg_loss | -11.0120 |
| avg_hold_time_bars | 2.3950 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
