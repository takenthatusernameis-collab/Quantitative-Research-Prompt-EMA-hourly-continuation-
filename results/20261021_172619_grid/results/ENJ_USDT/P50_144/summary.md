# EMA Hourly Continuation — ENJ/USDT P50_144

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7413 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.7121 |
| sortino_ratio | -0.4442 |
| max_drawdown | 0.4141 |
| cagr | -0.1853 |
| net_avg_win | 72.3039 |
| net_avg_loss | -90.7259 |
| avg_hold_time_bars | 21.1657 |
| exposure | 0.3180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
