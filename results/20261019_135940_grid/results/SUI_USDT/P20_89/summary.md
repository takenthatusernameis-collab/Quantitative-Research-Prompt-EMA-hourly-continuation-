# EMA Hourly Continuation — SUI/USDT P20_89

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.5829 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -5.4786 |
| sortino_ratio | -2.0937 |
| max_drawdown | 0.9327 |
| cagr | -0.6514 |
| net_avg_win | 37.7467 |
| net_avg_loss | -53.6767 |
| avg_hold_time_bars | 10.3636 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
