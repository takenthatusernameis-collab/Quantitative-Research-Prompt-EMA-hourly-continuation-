# EMA Hourly Continuation — ID/USDT P20_89

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -3.1722 |
| sortino_ratio | -1.1455 |
| max_drawdown | 0.7557 |
| cagr | -0.4175 |
| net_avg_win | 47.1345 |
| net_avg_loss | -66.5027 |
| avg_hold_time_bars | 13.4536 |
| exposure | 0.4000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
