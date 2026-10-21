# EMA Hourly Continuation — WIN/USDT P20_89

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -2.1445 |
| sortino_ratio | -0.6310 |
| max_drawdown | 0.5921 |
| cagr | -0.2521 |
| net_avg_win | 59.6045 |
| net_avg_loss | -82.7974 |
| avg_hold_time_bars | 20.1256 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
