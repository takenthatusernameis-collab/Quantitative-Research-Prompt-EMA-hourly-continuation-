# EMA Hourly Continuation — AIOZ/USDT P12_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7775 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.3410 |
| sortino_ratio | -0.8733 |
| max_drawdown | 0.6546 |
| cagr | -0.3317 |
| net_avg_win | 67.4187 |
| net_avg_loss | -80.8303 |
| avg_hold_time_bars | 9.5278 |
| exposure | 0.2962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
