# EMA Hourly Continuation — NFT/USDT P26_200

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.3946 |
| net_win_rate | 0.3629 |
| gross_profit_factor | 0.6171 |
| gross_win_rate | 0.3629 |
| sharpe_ratio | -5.9240 |
| sortino_ratio | -1.6141 |
| max_drawdown | 0.8567 |
| cagr | -0.5325 |
| net_avg_win | 42.3932 |
| net_avg_loss | -61.1838 |
| avg_hold_time_bars | 32.9695 |
| exposure | 0.5410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
