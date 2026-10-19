# EMA Hourly Continuation — APT/USDT P12_26

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1400 |
| net_profit_factor | 0.3116 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -12.0894 |
| sortino_ratio | -6.3972 |
| max_drawdown | 0.9998 |
| cagr | -0.9633 |
| net_avg_win | 7.8287 |
| net_avg_loss | -17.6672 |
| avg_hold_time_bars | 2.8886 |
| exposure | 0.1838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
