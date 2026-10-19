# EMA Hourly Continuation — WLD/USDT P12_144

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8545 |
| net_win_rate | 0.5181 |
| gross_profit_factor | 1.0872 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -1.0572 |
| sortino_ratio | -0.3164 |
| max_drawdown | 0.4074 |
| cagr | -0.1408 |
| net_avg_win | 81.2433 |
| net_avg_loss | -102.2225 |
| avg_hold_time_bars | 34.0928 |
| exposure | 0.6850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
