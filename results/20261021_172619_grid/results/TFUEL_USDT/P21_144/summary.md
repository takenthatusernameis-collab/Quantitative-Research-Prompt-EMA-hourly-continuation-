# EMA Hourly Continuation — TFUEL/USDT P21_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -3.7228 |
| sortino_ratio | -1.2067 |
| max_drawdown | 0.7616 |
| cagr | -0.4260 |
| net_avg_win | 55.5318 |
| net_avg_loss | -67.5457 |
| avg_hold_time_bars | 18.0247 |
| exposure | 0.4298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
