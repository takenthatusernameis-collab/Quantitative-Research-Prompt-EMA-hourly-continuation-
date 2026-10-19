# EMA Hourly Continuation — BTT/USDT P26_144

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4120 |
| net_win_rate | 0.3820 |
| gross_profit_factor | 0.8028 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -7.2948 |
| sortino_ratio | -2.2273 |
| max_drawdown | 0.9462 |
| cagr | -0.6877 |
| net_avg_win | 37.2466 |
| net_avg_loss | -55.8744 |
| avg_hold_time_bars | 24.0794 |
| exposure | 0.5100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
