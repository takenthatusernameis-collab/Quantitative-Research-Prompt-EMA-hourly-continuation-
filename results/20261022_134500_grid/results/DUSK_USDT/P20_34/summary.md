# EMA Hourly Continuation — DUSK/USDT P20_34

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.4752 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -9.2861 |
| sortino_ratio | -4.3202 |
| max_drawdown | 0.9956 |
| cagr | -0.8843 |
| net_avg_win | 19.7262 |
| net_avg_loss | -29.9690 |
| avg_hold_time_bars | 2.7899 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
