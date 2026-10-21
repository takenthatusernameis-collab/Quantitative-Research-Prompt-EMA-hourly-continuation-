# EMA Hourly Continuation — NFT/USDT P12_200

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.4487 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.6851 |
| gross_win_rate | 0.3770 |
| sharpe_ratio | -5.5930 |
| sortino_ratio | -1.5465 |
| max_drawdown | 0.8439 |
| cagr | -0.5184 |
| net_avg_win | 48.5011 |
| net_avg_loss | -65.4185 |
| avg_hold_time_bars | 37.3797 |
| exposure | 0.6355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
