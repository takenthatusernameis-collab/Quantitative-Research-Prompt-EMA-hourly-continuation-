# EMA Hourly Continuation — ACE/USDT P12_89

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.7836 |
| sortino_ratio | -0.9583 |
| max_drawdown | 0.6751 |
| cagr | -0.3565 |
| net_avg_win | 54.2461 |
| net_avg_loss | -71.6868 |
| avg_hold_time_bars | 20.1392 |
| exposure | 0.5368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
