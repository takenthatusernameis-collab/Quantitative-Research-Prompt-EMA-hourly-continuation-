# EMA Hourly Continuation — XCH/USDT P144_200

**Symbol:** XCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.4081 |
| net_win_rate | 0.4163 |
| gross_profit_factor | 0.8010 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -5.3919 |
| sortino_ratio | -1.5409 |
| max_drawdown | 0.8503 |
| cagr | -0.5305 |
| net_avg_win | 34.6826 |
| net_avg_loss | -60.6076 |
| avg_hold_time_bars | 4.4261 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
