# EMA Hourly Continuation — ZEC/USDT P21_34

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.6925 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -1.6937 |
| sortino_ratio | -0.3743 |
| max_drawdown | 0.3625 |
| cagr | -0.1578 |
| net_avg_win | 68.5945 |
| net_avg_loss | -91.8612 |
| avg_hold_time_bars | 5.6192 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
