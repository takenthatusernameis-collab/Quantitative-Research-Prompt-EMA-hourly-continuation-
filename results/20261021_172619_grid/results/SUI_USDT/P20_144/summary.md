# EMA Hourly Continuation — SUI/USDT P20_144

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.9119 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.0977 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -0.5385 |
| sortino_ratio | -0.1527 |
| max_drawdown | 0.3192 |
| cagr | -0.0719 |
| net_avg_win | 87.0983 |
| net_avg_loss | -105.3738 |
| avg_hold_time_bars | 27.3127 |
| exposure | 0.4805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
