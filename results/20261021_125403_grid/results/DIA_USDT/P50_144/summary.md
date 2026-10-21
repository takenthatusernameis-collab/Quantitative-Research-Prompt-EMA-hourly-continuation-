# EMA Hourly Continuation — DIA/USDT P50_144

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8692 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1151 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.8236 |
| sortino_ratio | -0.2365 |
| max_drawdown | 0.3372 |
| cagr | -0.1056 |
| net_avg_win | 77.2916 |
| net_avg_loss | -100.3333 |
| avg_hold_time_bars | 15.0779 |
| exposure | 0.2716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
