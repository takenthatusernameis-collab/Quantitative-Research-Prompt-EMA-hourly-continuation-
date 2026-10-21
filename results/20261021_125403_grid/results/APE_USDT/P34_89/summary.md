# EMA Hourly Continuation — APE/USDT P34_89

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.8943 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.3869 |
| sortino_ratio | -0.7125 |
| max_drawdown | 0.5749 |
| cagr | -0.2793 |
| net_avg_win | 60.8051 |
| net_avg_loss | -79.3655 |
| avg_hold_time_bars | 10.4932 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
