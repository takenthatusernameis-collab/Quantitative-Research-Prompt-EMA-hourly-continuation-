# EMA Hourly Continuation — APT/USDT P12_21

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6433 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.3787 |
| sortino_ratio | -0.5643 |
| max_drawdown | 0.4920 |
| cagr | -0.2280 |
| net_avg_win | 66.8231 |
| net_avg_loss | -91.7748 |
| avg_hold_time_bars | 5.1418 |
| exposure | 0.0643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
