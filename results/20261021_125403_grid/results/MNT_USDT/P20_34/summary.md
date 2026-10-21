# EMA Hourly Continuation — MNT/USDT P20_34

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5972 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.5045 |
| sortino_ratio | -0.9977 |
| max_drawdown | 0.7000 |
| cagr | -0.3684 |
| net_avg_win | 53.4151 |
| net_avg_loss | -83.7169 |
| avg_hold_time_bars | 5.8244 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
