# EMA Hourly Continuation — W/USDT P26_144

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.8866 |
| net_win_rate | 0.5389 |
| gross_profit_factor | 1.1751 |
| gross_win_rate | 0.5410 |
| sharpe_ratio | -0.8033 |
| sortino_ratio | -0.2545 |
| max_drawdown | 0.3336 |
| cagr | -0.1160 |
| net_avg_win | 79.2023 |
| net_avg_loss | -104.4171 |
| avg_hold_time_bars | 22.0615 |
| exposure | 0.4894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
