# EMA Hourly Continuation — WIN/USDT P26_50

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8545 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -3.2742 |
| sortino_ratio | -0.8630 |
| max_drawdown | 0.6464 |
| cagr | -0.3265 |
| net_avg_win | 49.7229 |
| net_avg_loss | -77.6303 |
| avg_hold_time_bars | 6.8872 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
